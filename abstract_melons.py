class AbstractMelonOrder(object):
    """ Domestic and international melon orders"""

    def __init__(self, species, qty, country_code, tax, order_type):
        """Initializes melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.tax = tax
        self.order_type = order_type


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == 'Christmas melons':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, "US", 0.08, "domestic")



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, country_code, 0.17, "international")

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            return total + 3
        else:
            return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty, country_code):
        super(GovernmentMelonOrder, self).__init__(species, qty, country_code, 0, "government")
        self.passed_inspection = False

    def marked_inspection(self, passed=True):
        self.passed_inspection = passed



dom_melons = DomesticMelonOrder('cremshaw', 5)
int_melons = InternationalMelonOrder('watermelon', 10, "GB")
less_int_melon = InternationalMelonOrder('Christmas melons', 9, "GB")
gov_melon = GovernmentMelonOrder('Yellow', 10, "GB")

print dom_melons
print int_melons
print less_int_melon
print gov_melon
