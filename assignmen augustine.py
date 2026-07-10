class Staff:
    def __init__(self, s_name, access_code):
        self.s_name = s_name
        self.__access_code = access_code

    @property
    def access_code(self):
        return self.__access_code

    @access_code.setter
    def access_code(self, new_code):
        if len(new_code) >= 4:
            self.__access_code = new_code
            print("Access code updated successfully.")
        else:
            print("Error: Access code must be at least 4 characters long.")

    # Method to display staff information
    def display_info(self):
        print(f"Staff Name: {self.s_name}")
        print("Access Code: [Protected]")  # Do not expose directly



staff1 = Staff("Alice", "1234")
staff1.display_info()

print("Current Access Code:", staff1.access_code)

staff1.access_code = "5678"  
staff1.access_code = "12"
