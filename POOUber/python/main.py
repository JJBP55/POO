from car import Car

if __name__ == "__main__":
        print("Hola mundo");
        car = Car()
        car.license = "AMS234"
        car.driver = "Andres herrera"
        print (vars(car))

        car2 = Car()
        car2.license = "QWE567"
        car2.driver = "Andrea herrera"
        print (vars(car2))

