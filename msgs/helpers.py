from django.template.defaultfilters import slugify

def SlugifyUniquely(value, model, slugfield="slug"):
    """Returns a slug on a name which is unique within a model's table
    """
    suffix = 0
    potential = base = slugify(value)

    while True:
        if suffix:
            potential = "-".join([base, str(suffix)])

        if not model.objects.filter(**{slugfield: potential}).exists():
            return potential
            # we hit a conflicting slug, so bump the suffix & try again
        suffix += 1


