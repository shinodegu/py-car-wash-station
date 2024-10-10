class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: int) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_ratings: int) -> None:
        self.distance_center = distance_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_ratings

    def calculate_washing_price(self, car_info: callable) -> float:
        return round((car_info.comfort_class
                      * (self.clean_power - car_info.clean_mark)
                      * self.average_rating / self.distance_center), 1)

    def serve_cars(self, teh_card: list) -> float:
        price = 0
        for cars in teh_card:
            if cars.clean_mark <= self.clean_power:
                price += self.calculate_washing_price(cars)
                self.wash_single_car(cars)
        return price

    def wash_single_car(self, dirty_car: set) -> None:
        if self.clean_power > dirty_car.clean_mark:
            dirty_car.clean_mark = self.clean_power

    def rate_service(self, grade: int) -> None:
        self.average_rating = round((self.count_of_ratings
                                     * self.average_rating + grade)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
