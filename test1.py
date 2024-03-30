#chia dãy số thành ba phần truyền vào class để đọc ba phần đó rồi thêm nghìn triệu nếu hàm đó có >3 kí tự
def split_into_parts(number):

    number_str = str(number)

    length = len(number_str)

    parts_dict = {}

    if length <= 3:
        parts_dict['part1'] = number_str[:length]

    elif length <= 6:
        parts_dict['part1'] = number_str[:length - 3]
        parts_dict['part2'] = number_str[length - 3:length]

    else:
        parts_dict['part1'] = number_str[:length - 6]
        parts_dict['part2'] = number_str[length - 6:length - 3]
        parts_dict['part3'] = number_str[length - 3:]

    return parts_dict

input_number = int(input("number = "))

result = split_into_parts(input_number)

number_string_name = {"1":"một",
                      "2":"hai",
                      "3":"ba",
                      "4":"bốn",
                      "5":"năm",
                      "6":"sáu",
                      "7":"bảy",
                      "8":"tám",
                      "9":"chín",
                      "0":"không",
                    }
class Number_string():
    def __init__(self, numbers) -> None:
        self.numbers = numbers
    def number_to_array(self):
        number_array = []
        for i in str(self.numbers):
            for j in number_string_name.keys():
                if i == j :
                    number_array.append(number_string_name[j])
        return number_array
    def three_digit(self):
        values_array = self.number_to_array()
        if self.numbers == 100:
            return "một trăm"
        elif self.numbers % 100 < 10:
            return values_array[len(values_array)-3] + " trăm linh " + self.one_digit()
        elif values_array[len(values_array)-2] == "một":
            if values_array[len(values_array)-1] == "năm":
                return values_array[len(values_array)-3] + " trăm mười lăm"
            else:
                return values_array[len(values_array)-3] + " trăm mười " + self.one_digit()
        else :
            return values_array[len(values_array)-3] + " trăm " + self.two_digit()

    def two_digit(self):
        values_array = self.number_to_array()

        if self.numbers >= 10 and self.numbers < 20:
            if self.numbers == 10:
                return "mười"
            elif self.numbers == 15:
                return "mười lăm"
            else :
                return "mười " + self.one_digit()
        elif self.numbers % 10 == 4:
            return values_array[len(values_array)-2] + " mươi tư"
        elif self.numbers % 10 == 5:
            return values_array[len(values_array)-2] + " mươi lăm"
        else :
            return values_array[len(values_array)-2] + " mươi " + self.one_digit()
    def one_digit(self):
        values_array = self.number_to_array()
        return values_array[len(values_array)-1]

# print(result["part1"])

number_string = Number_string(int(result["part1"]))

print(number_string.three_digit())