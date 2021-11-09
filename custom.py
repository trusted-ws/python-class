class Automatic(type):
    def __new__(mcls, name, bases, attrs, **kwargs):
        attrs['__class_name__'] = name
        return type(name, bases, attrs)

def set_attributes(obj: object, props: dict, cls_name: str = None, **kwargs):
    props_list = [
        item for sublist in [
            list(props.get(m).keys()) for m in [
                a for a in props.keys()
            ]
        ] for item in sublist
    ]

    for p in props.keys():
        for prop_name, prop_type in props[p].items():
            if prop_name in kwargs.keys():
                if prop_type == type(kwargs.get(prop_name)):                 
                    source = obj.__class__ if not hasattr(obj, '__bases__') else obj
                    attr_name = prop_name

                    if p == 'private':
                        if not cls_name:
                            attr_name = f'_{source.__name__.lstrip("_")}__{prop_name}'
                        else:
                            attr_name = f'_{cls_name}__{prop_name}'

                    setattr(obj, attr_name, kwargs.get(prop_name))
                    props_list.pop(props_list.index(prop_name))
                else:
                    raise TypeError(f'Property {prop_name!r} must be {props[p].get(prop_name).__name__!r}, given {type(kwargs.get(prop_name)).__name__!r}.')
    
    if len(props_list):
        raise TypeError(f'Missing properties: {", ".join(props_list)!r} for class {obj.__class__.__name__!r}')