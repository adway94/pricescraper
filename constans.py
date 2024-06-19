#Actualizar si se suma un super y tener presente el nombre a la hora de escribir debe matchear con la funcion
STORES = ["alvear", "carrefour", "changomas", "dia", "jumbo", "la_anonima", "coto"] 

#Nombre del archivo donde se va  aguardar la data
FILE_NAME = "historic_prices"

CARREFOUR = {
    "NOT CO BURGER 160GR" : "https://www.carrefour.com.ar/medallon-not-burger-premium-flow-pack-2-uni-721929/p",
    "VEGETALEX BURGER" : "https://www.carrefour.com.ar/medallon-de-vegetal-burguer-vegetalex-2-uni-734579/p",
    "HAMBURGUESA PALADINI VEGETAL 2U 160GR" : "https://www.carrefour.com.ar/medallon-paladini-100-vegetal-x-2-uni-704482/p"
}

DIA = {
    "NOT CO BURGER 160GR" : "https://diaonline.supermercadosdia.com.ar/medallon-vegetal-not-burger-notco-80-gr-17147/p"
}

COTO = {
    "NOT CO BURGER 160GR" : "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-medallon-a-base-de-vegetal-x2-not-burger-160g/_/A-00565701-00565701-200",
    "VEGETALEX BURGER" : "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-burger-de-origen-vegetal-vegetalex-226g/_/A-00578568-00578568-200"
}

LA_ANONIMA = {
    "NOT CO BURGER 160GR" : "https://supermercado.laanonimaonline.com/congelados/hamburguesas/vegetales-y-otros/medallon-a-base-de-proteina-vegetal-x-2-un-not-burger-x-160-g/art_24588/",
    "VEGETALEX BURGER" : "https://supermercado.laanonimaonline.com/congelados/hamburguesas/burger-vegetal-x-2-un-vegetalex-x-226-g/art_26731/"
}

ALVEAR = {
    "API" :  {
        "URL" : "https://alvearonline.com.ar:9993/api/Catalogo/GetCatalagoSeleccionado?idCatalogo=1042&subfiltros=&page=1&pageSize=40&idInstalacion=3&idSubrubro=2192&esRubro=false&vistaFavoritos=false",
        "PRODUCT" :  {"NOT CO BURGER 160GR" : 70693, 
                 "HAMBURGUESA PALADINI VEGETAL 2U 160GR" : 68320, 
                 "MEDALLON FELICES LAS VACAS KARNEVIL 2U 160GR" : 70038}
    }
}

CHANGOMAS = {
    "NOT CO BURGER 160GR" : "https://www.masonline.com.ar/medallon-vegetal-not-burguer-160g-2u/p",
    "VEGETALEX BURGUER" : "https://www.masonline.com.ar/medallones-vegetalex-origen-vegetal-226-g-2u/p",
    "HAMBURGUESA PALADINI VEGETAL 2U 160GR" : "https://www.masonline.com.ar/hamburguesa-100-vegetal-paladini-160g-2u/p"
}

JUMBO = {
    "NOT CO BURGER 160GR" : "https://www.jumbo.com.ar/api/catalog_system/pub/products/search?fq=skuId:339066"
}