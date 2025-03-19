from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'
CURRENT_DATE = datetime.now().date()


class Passport:

    """
    initiating a value count for the passport number
    """
    initial_passport_number = 0

    def __init__(self, first_name, last_name, dob, country, exp_date):
        """
        Initiated the values and assigned to the object properties.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.dob = datetime.strptime(dob, DATE_FORMAT).date()
        self.country: str = country
        self.exp_date = datetime.strptime(exp_date, DATE_FORMAT).date()
        self.countries_visited_list = []
        self.time_countries_visited_list = []
        self.passport_id = Passport.initial_passport_number
        Passport.initial_passport_number += 1
        pass

    def is_valid(self):
        """
        Checking the expiry date with the current date for Passport Validity.
        """
        return self.exp_date >= CURRENT_DATE

    def summary(self):
        """
        summary with human-readable information about the passport. 
        The output should follow the pattern: 
        `This passport belongs to Alan Turing, born on 1912-06-23 in The United Kingdom. 
        It is invalid.`. Make sure to include whether the passport is valid or not with the phrase 'It is valid' or 'It is invalid', by using the `is_valid` method for this.
        """
        valid_passport = "invalid"
        if self.is_valid():
            valid_passport = "valid"
        return (f"This passport belongs to {self.first_name} {self.last_name}, born on {self.dob} in {self.country}. It is {valid_passport}")

    def check_data(self, first_name: str, last_name: str, input_dob, country: str):
        """
        Validating the passport data based on the input data.
        """
        return (
            self.first_name.lower() == first_name.lower()
            and self.last_name.lower() == last_name.lower()
            and self.dob == datetime.strptime(input_dob, DATE_FORMAT).date()
            and self.country.lower() == country.lower()
            and self.is_valid())

    def stamp(self, country: str):
        """
        Recording the visited   country other than passport issued country.
        """
        if (self.country.lower() != country.lower()):
            if (country not in self.countries_visited_list):
                self.countries_visited_list.append(country)
            self.time_countries_visited_list.append(country)

    def countries_visited(self):
        """
        Returns the countries list which is visited 
        """
        return self.countries_visited_list

    def times_visited(self, country: str):
        """
        Returns the number of times that country has been visited or stamped.
        """
        return self.time_countries_visited_list.count(country)

    def sum_square_visits(self):
        """
        Returns: sum of squares of the times_visited over each visited country
        """
        countries_visited = self.time_countries_visited_list
        country_count = {}
        for country in countries_visited:
            country_count[country] = country_count.get(country, 0) + 1
        sum_square = 0
        for value in country_count.values():
            sum_square += (value ** 2)

        return sum_square

    def passport_number(self):
        """
        Returns the passport number id number 
        """
        return self.passport_id


if __name__ == "__main__":
    # Create instances of the Passport class here to try out its methods!
    Ragul = Passport(
                "Ragul",
                "Arulanandam",
                "2000-01-27",
                "India",
                "2024-12-31")
    print("The Passport Number", Ragul.passport_number)
    print(Ragul.summary())
    print(Ragul.check_data("Ragul", "Arulanandam", "2000-01-27", "India"))
    Ragul.stamp("France")
    Ragul.stamp("UK")
    Ragul.stamp("US")
    print("Countries Visited", Ragul.countries_visited())
    print("No. Of. Time Visited to the countries UK", Ragul.times_visited("Italy"))
    print("Sum of the square visits", Ragul.sum_square_visits())
