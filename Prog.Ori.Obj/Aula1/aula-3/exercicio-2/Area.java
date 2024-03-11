public class Area {

    Float base;
    Float altura;

    public Area(String base_string, String altura_string){
        this.base = Float.parseFloat(base_string);
        this.altura = Float.parseFloat(altura_string);
    }

    public Area(int base, int altura){
        float b;
        float a;

        b = base;
        a = altura;
        this.base = b;
        this.altura = a;
    }
    public Area(Float base, Float altura){
        this.base = base;
        this.altura = altura;
    }
    public Float areaTriangulo(Float base,Float altura){
        return (base * altura)/2;
    }
    public Float areaQuadrado(Float base, Float altura){
        return base * altura;
    }
}
