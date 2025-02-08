from django import template

register = template.Library()

@register.filter
def format_price(value):
    try:
        # Conver to integer first to remove any decimal places
        value = int(value)
        # Formt with thousand separator
        return f"{value:,}".replace(',', '.')
    except (ValueError, TypeError):
        return value