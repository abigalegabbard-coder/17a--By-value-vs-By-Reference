# Primitive Types: int, str, bool, float, dict?

# passed "by value" - means a copy of the value is given
# changes are not reflected in the source
def primitive_int(val: int):
    val += 1


def primitive_str(val: str):
    val += "I was changed"


def primitive_bool(val: bool):
    val = not val


def primitive_float(val: float):
    val += 1


# Dictionary - NOT primitive - a complex type, PASSED BY REFERENCE
def not_primitive_dict(val: dict):
    val["updated"] = True


# List - NOT primitive - a complex type, PASSED BY REFERENCE
def not_primitive_list(val: list):
    val.append("Added")


def main():
    my_int = 1
    primitive_int(my_int)
    print(f"My int was 1, after funtion it is {my_int}")

    my_str = "Hello"
    primitive_str(my_str)
    print(f"My str was \"Hello\", after funtion it is {my_str}")

    my_bool = True
    primitive_int(my_bool)
    print(f"My bool was True, after funtion it is {my_bool}")

    my_float = 1.1
    primitive_float(my_float)
    print(f"My float was 1.1, after funtion it is {my_float}")

    my_dict = {"updated": False}
    not_primitive_dict(my_dict)
    print(f"My dict was {{\"updated\": False}}, after funtion it is {my_dict}")

    my_list = [1,2,3]
    not_primitive_list(my_list)
    print(f"My list was [1,2,3], after the function it is {my_list}")

if __name__ == "__main__":
    main()

#def update_summary(dict)
#   determine if the key exists already, if so add to the values stored
#   if not, create the record

mykytas_list = [[],[[],[],[[],[[],[],[5]],[]]],[],[],[]]
print(mykytas_list[1][2][1][2][0])