class uberPool extends Car{
    String brand;
    String model;

    public uberPool(String license, Account driver, String brand, String model){
        super(license, driver);
        this.brand = brand;
        this.model = model;
    }
}