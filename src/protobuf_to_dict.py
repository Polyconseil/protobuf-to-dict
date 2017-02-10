from google.protobuf import message
from google.protobuf import descriptor


__all__ = ["protobuf_to_dict", "TYPE_CALLABLE_MAP", "dict_to_protobuf", "REVERSE_TYPE_CALLABLE_MAP"]


EXTENSION_CONTAINER = '___X'


TYPE_CALLABLE_MAP = {
    descriptor.FieldDescriptor.TYPE_DOUBLE: float,
    descriptor.FieldDescriptor.TYPE_FLOAT: float,
    descriptor.FieldDescriptor.TYPE_INT32: int,
    descriptor.FieldDescriptor.TYPE_INT64: int,
    descriptor.FieldDescriptor.TYPE_UINT32: int,
    descriptor.FieldDescriptor.TYPE_UINT64: int,
    descriptor.FieldDescriptor.TYPE_SINT32: int,
    descriptor.FieldDescriptor.TYPE_SINT64: int,
    descriptor.FieldDescriptor.TYPE_FIXED32: int,
    descriptor.FieldDescriptor.TYPE_FIXED64: int,
    descriptor.FieldDescriptor.TYPE_SFIXED32: int,
    descriptor.FieldDescriptor.TYPE_SFIXED64: int,
    descriptor.FieldDescriptor.TYPE_BOOL: bool,
    descriptor.FieldDescriptor.TYPE_STRING: str,
    descriptor.FieldDescriptor.TYPE_BYTES: lambda b: b.decode(encoding='utf-8'),
    descriptor.FieldDescriptor.TYPE_ENUM: int,
}


def repeated(type_callable):
    return lambda value_list: [type_callable(value) for value in value_list]


def enum_label_name(field, value):
    return field.enum_type.values_by_number[int(value)].name


def protobuf_fields_to_dict(fields, pb, type_callable_map, use_enum_labels, including_default_value_fields):
    result_dict = {}
    extensions = {}

    for field, value in fields:
        type_callable = _get_field_value_adaptor(
            pb, field, type_callable_map, use_enum_labels, including_default_value_fields)
        if field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
            type_callable = repeated(type_callable)

        if field.is_extension:
            extensions[str(field.number)] = type_callable(value)
            continue

        result_dict[field.name] = type_callable(value)

    if extensions:
        result_dict[EXTENSION_CONTAINER] = extensions

    return result_dict


def protobuf_to_dict(
        pb, type_callable_map=TYPE_CALLABLE_MAP, use_enum_labels=False, including_default_value_fields=False):
    if including_default_value_fields:
        return protobuf_fields_to_dict(
            [(field, getattr(pb, field.name)) for field in pb.DESCRIPTOR.fields],
            pb, type_callable_map, use_enum_labels, including_default_value_fields)
    return protobuf_fields_to_dict(
        pb.ListFields(), pb, type_callable_map, use_enum_labels, including_default_value_fields)


def _get_field_value_adaptor(
        pb, field, type_callable_map=TYPE_CALLABLE_MAP, use_enum_labels=False, including_default_value_fields=False):
    if field.type == descriptor.FieldDescriptor.TYPE_MESSAGE:
        # recursively encode protobuf sub-message
        return lambda pb: protobuf_to_dict(
            pb,
            type_callable_map=type_callable_map,
            use_enum_labels=use_enum_labels,
            including_default_value_fields=including_default_value_fields
        )

    if use_enum_labels and field.type == descriptor.FieldDescriptor.TYPE_ENUM:
        return lambda value: enum_label_name(field, value)

    if field.type in type_callable_map:
        return type_callable_map[field.type]

    raise TypeError("Field %s.%s has unrecognised type id %d" % (
        pb.__class__.__name__, field.name, field.type))


def get_bytes(value):
    return value.encode('utf-8')


REVERSE_TYPE_CALLABLE_MAP = {
    descriptor.FieldDescriptor.TYPE_BYTES: get_bytes,
}


def dict_to_protobuf(pb_klass_or_instance, values, type_callable_map=REVERSE_TYPE_CALLABLE_MAP, strict=True):
    """Populates a protobuf model from a dictionary.

    :param pb_klass_or_instance: a protobuf message class, or an protobuf instance
    :type pb_klass_or_instance: a type or instance of a subclass of google.protobuf.message.Message
    :param dict values: a dictionary of values. Repeated and nested values are
       fully supported.
    :param dict type_callable_map: a mapping of protobuf types to callables for setting
       values on the target instance.
    :param bool strict: complain if keys in the map are not fields on the message.
    """
    if isinstance(pb_klass_or_instance, message.Message):
        instance = pb_klass_or_instance
    else:
        instance = pb_klass_or_instance()
    return _dict_to_protobuf(instance, values, type_callable_map, strict)


def _get_field_mapping(pb, dict_value, strict):
    field_mapping = []
    for key, value in dict_value.items():
        if key == EXTENSION_CONTAINER:
            continue
        if key not in pb.DESCRIPTOR.fields_by_name:
            if strict:
                raise KeyError("%s does not have a field called %s" % (pb, key))
            continue
        field_mapping.append((pb.DESCRIPTOR.fields_by_name[key], value, getattr(pb, key, None)))

    for ext_num, ext_val in dict_value.get(EXTENSION_CONTAINER, {}).items():
        try:
            ext_num = int(ext_num)
        except ValueError:
            raise ValueError("Extension keys must be integers.")
        if ext_num not in pb._extensions_by_number:
            if strict:
                raise KeyError(
                    "%s does not have a extension with number %s. Perhaps you forgot to import it?" % (pb, key)
                )
            continue
        ext_field = pb._extensions_by_number[ext_num]
        pb_val = None
        pb_val = pb.Extensions[ext_field]
        field_mapping.append((ext_field, ext_val, pb_val))

    return field_mapping


def _dict_to_protobuf(pb, value, type_callable_map, strict):
    fields = _get_field_mapping(pb, value, strict)

    for field, input_value, pb_value in fields:
        if field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
            for item in input_value:
                if field.type == descriptor.FieldDescriptor.TYPE_MESSAGE:
                    m = pb_value.add()
                    _dict_to_protobuf(m, item, type_callable_map, strict)
                elif field.type == descriptor.FieldDescriptor.TYPE_ENUM and isinstance(item, str):
                    pb_value.append(_string_to_enum(field, item))
                else:
                    pb_value.append(item)
            continue
        if field.type == descriptor.FieldDescriptor.TYPE_MESSAGE:
            _dict_to_protobuf(pb_value, input_value, type_callable_map, strict)
            continue

        if field.type in type_callable_map:
            input_value = type_callable_map[field.type](input_value)

        if field.is_extension:
            pb.Extensions[field] = input_value
            continue

        if field.type == descriptor.FieldDescriptor.TYPE_ENUM and isinstance(input_value, str):
            input_value = _string_to_enum(field, input_value)

        setattr(pb, field.name, input_value)

    return pb


def _string_to_enum(field, input_value):
    enum_dict = field.enum_type.values_by_name
    try:
        input_value = enum_dict[input_value].number
    except KeyError:
        raise KeyError("`%s` is not a valid value for field `%s`" % (input_value, field.name))
    return input_value
