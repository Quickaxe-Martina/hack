def update_from_dict(instance, attrs, commit):

    field_names = list(map(lambda f: f.name, instance._meta.get_fields()))
    for attr, val in attrs.items():
        if attr in field_names:
            setattr(instance, attr, val)

    if commit:
        instance.save()
