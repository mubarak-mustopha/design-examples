def make_object(**kwargs):
    private = kwargs

    def getter(key):
        return private[key]
    
    def setter(key, new_value):
        if key not in private:
            raise KeyError(key)    
        private[key] = new_value

    return {"get": getter, "set": setter}

object = make_object(name="Mubaarock", email="muby@gmail.com", age=23, department="SEN")
print("Name:", object["get"]("name"))
object["set"]("name", "Al-Mubaarock")
print("Name:", object["get"]("name"))
print("Department:", object["get"]("department"))
print("School:", object["get"]("school"))