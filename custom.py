class Automatic(type):
    def __new__(mcls, name, bases, attrs, **kwargs):
        attrs['__cls__'] = name
        return type(name, bases, attrs)


def set_attributes(obj: object, props: dict, cls_name: str, *args, **kwargs):

    props_list = [
        item for sublist in [
            list(props.get(m).keys()) for m in [
                a for a in props.keys()
            ]
        ] for item in sublist
    ]

    arguments = {}
    counter = 0

    if len(kwargs) > 0:
        for key, value in kwargs.items():
            if key in props_list:
                arguments[key] = value

    if len(args) > 0:
        for i in props_list:
            try:
                if i in kwargs.keys():
                    continue

                arguments[i] = args[counter]
                counter += 1

            except IndexError:
                raise ValueError(f'There\'s no default value for {i!r}.')
    else:
        arguments = kwargs.copy()

    for p in props.keys():
        for prop_name, prop_type in props[p].items():
            if prop_name in arguments.keys():
                if prop_type == type(arguments.get(prop_name)):                 
                    source = obj.__class__ if not hasattr(obj, '__bases__') else obj
                    attr_name = prop_name

                    if p == 'private':
                        if not cls_name:
                            attr_name = f'_{source.__name__.lstrip("_")}__{prop_name}'
                        else:
                            attr_name = f'_{cls_name}__{prop_name}'

                    setattr(obj, attr_name, arguments.get(prop_name))
                    props_list.pop(props_list.index(prop_name))
                else:
                    raise TypeError(f'Property {prop_name!r} must be {props[p].get(prop_name).__name__!r}, not {type(arguments.get(prop_name)).__name__!r}.')
    
    if len(props_list):
        props_list_formatted = [f'{x!r}' for x in props_list]
        raise TypeError(f'Missing properties: {", ".join(props_list_formatted)} for class {obj.__class__.__name__!r}.')
