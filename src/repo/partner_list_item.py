class PartnerListItem:
    def __init__(self,
                 id,
                 type_name,
                 partner_name,
                 director_name,
                 phone,
                 rating,
                 discount=0):
        self.id = id
        self.type_name = type_name
        self.partner_name = partner_name
        self.director_name = director_name
        self.phone = phone
        self.rating = rating
        self.discount = discount

    @property
    def partner_display_name(self):
        return f"{self.type_name} | {self.partner_name}"

    # Свойство используется для формирования человекочитаемого значения
    @property
    def discount_display_value(self):
        return f"{self.discount}%"

    # Свойство используется для формирования человекочитаемого значения
    @property
    def rating_display_value(self):
        return f"Рейтинг: {self.rating}"
