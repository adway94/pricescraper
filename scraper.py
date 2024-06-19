import json

import pandas as pd
import regex as re
import requests
from bs4 import BeautifulSoup
import time

from datetime import datetime
from constans import *

class FullMetalScraper():
    def __init__ (self):
        self.columns = ['store', 'product', 'price', 'date']
    @staticmethod
    def execution_time(func):
        """
        Decorator to measure the execution time of a function.
        Args:
            func: The function to be decorated.

        Returns:
            A wrapper function that measures the execution time of the decorated function.
        """
        def wrapper(self, *args, **kwargs):
            start = time.time()
            result = func(self, *args, **kwargs)  # Call the decorated function
            end = time.time()
            execution_time = end - start
            print(f"El tiempo de ejecucion fue de: {execution_time} segundos")
            return result
        return wrapper
    
    def get_dia_prices(self):
        #Dia
        products_with_prices = []
        
        for product in DIA:
            try:
                response = requests.get(DIA[product])
                html_content = response.content

                soup = BeautifulSoup(html_content, 'html.parser')

                div_encontrado = soup.find('span', class_='vtex-product-price-1-x-currencyContainer').contents

                price = ""
                regex = '<span class="vtex-product-price-1-x-currency(.+?)">(.*?)</span>'

                for html in div_encontrado:
                    match = re.search(regex, str(html))
                    if match:
                        # Capture the content within the span
                        content = match.group(2)
                        # Concatenate the content to the price string
                        price += content

                regex = "\d+(.*?)\d+"
                match = re.search(regex, price)
                price = match.group(0)
                
                products_with_prices.append((product, price))
                print(f"El precio de {product} DIA es: {price}")
            except Exception as e:
                print(f"Error buscando en DIA producto: {product}. \n Error: {e}")
                
        return products_with_prices

    def get_carrefour_prices(self):
        #Carrefour
        products_with_prices = []
        
        for product in CARREFOUR:
            try:
                response = requests.get(CARREFOUR[product])
                html_content = response.content

                soup = BeautifulSoup(html_content, 'html.parser')

                div_encontrado = soup.find('span', class_='valtech-carrefourar-product-price-0-x-currencyContainer').contents

                price = ""
                regex = '<span class="valtech-carrefourar-product-price-0-x-currency(.+?)">(.*?)</span>'

                for html in div_encontrado:
                        match = re.search(regex, str(html))
                        if match:
                            # Capture the content within the span
                            content = match.group(2)
                            # Concatenate the content to the price string
                            price += content
                            
                regex = "\d+(.*?)\d+"
                match = re.search(regex, price)
                price = match.group(0)
                
                products_with_prices.append((product, price))
                print(f"El precio de {product} CARREFOUR es: {price}")
            except Exception as e:
                print(f"Error buscando en CARREFOUR producto: {product}. \n Error: {e}")
        
        return products_with_prices
    def get_la_anonima_prices(self):
        #La Anonima
        products_with_prices = []
        
        for product in LA_ANONIMA:
            try:
                response = requests.get(LA_ANONIMA[product])
                html_content = response.content

                soup = BeautifulSoup(html_content, 'html.parser')

                #Esta variable va a ser una lista de 2 elementos 1 elemento es el precio siendo str y la otro es un tag de html
                #haciendo referencia a los decimales
                div_encontrado = soup.find('div', class_='precio destacado').contents

                regex = "\d+(.*?)\d+"
                match = re.search(regex, div_encontrado[0])

                price = match.group(0)
                
                products_with_prices.append((product, price))
                print(f"El precio de {product} LA ANONIMA es: {price}")
            except Exception as e:
                print(f"Error buscando en LA ANONIMA producto: {product}. \n Error: {e}")
                
        return products_with_prices
    def get_alvear_prices(self):
        #Alvear
        #Esto tiene una API, esta api hay que ver el producto y buscar el que corresponda
        #posiblemente haya que modificar el id para bucar que onda
        response = requests.get(ALVEAR["API"]["URL"]).content 
        data = json.loads(response)

        articles_list = data["listadoSecciones"][0]["listaArticulos"]
        articles_list += data["listadoSecciones"][1]["listaArticulos"]
        
        products_with_prices = []

        for product in ALVEAR["API"]["PRODUCT"]:
            try:
                #Al buscar un id solo voy a obtener 1 articulo
                filtered_item = [item for item in articles_list if item["idArticulo"] == ALVEAR["API"]["PRODUCT"][product]][0] 

                price = filtered_item["precioLista"]

                products_with_prices.append((product, price))
                print(f"El precio de {product} ALVEAR es: {price}")
            except Exception as e:
                print(f"Error buscando en ALVEAR producto: {product}")
        
        return products_with_prices
    
    def get_changomas_prices(self):
        #Chango mas
        products_with_prices = []
        
        for product in CHANGOMAS:
            try:
                response = requests.get(CHANGOMAS[product])
                html_content = response.content
                
                soup = BeautifulSoup(html_content, 'html.parser')
                
                div_encontrado = soup.find('div', class_="valtech-gdn-dynamic-product-0-x-dynamicProductPrice mb4").contents
                
                price = " ".join(div_encontrado)
                regex = "\d+(.*?)\d+"
                match = re.search(regex, price)
                price = match.group(0)
                
                products_with_prices.append((product, price))
                print(f"El precio de {product} en CHANGO MAS es: {price}")
            except Exception as e:
                print(f"Error buscando en CHANGOMAS producto: {product}. \n Error: {e}")
        
        return products_with_prices
    
    def get_jumbo_prices(self):
        #Jumbo
        #Este es medio dolor de huevo, hay que ver la url ver como carajo sacar los sku para hacer el 
        #serch y esas cosas, va a tener que pensarse un poco, pero bueno no esta perdido (por ahora)
        products_with_prices = []
        for product in JUMBO:
            try:
                response = requests.get(JUMBO[product]).json()
                
                price = response[0]["items"][0]["sellers"][0]["commertialOffer"]["Price"]
                
                products_with_prices.append((product, price))
                print(f"El precio de {product} en Jumbo es: {price}")
            except Exception as e:
                print(f"Error buscando en JUMBO producto: {product}. \n Error: {e}")
        
        return products_with_prices
    
    def get_coto_prices(self):
        #COTO
        products_with_prices = []
        headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                    }
        for product in COTO:
            try:
                response = requests.get(COTO[product], headers=headers)
                html_content = response.content
                
                soup = BeautifulSoup(html_content, 'html.parser')
                div_encontrado = soup.find('span', class_="atg_store_newPrice").contents
                
                price = " ".join(div_encontrado)
                regex = "\d+(.*?)\d+"
                match = re.search(regex, price)
                price = match.group(0)
                
                products_with_prices.append((product, price))
                print(f"El precio de {product} en COTO es: {price}")           
            except Exception as e:
                print(f"Error buscando en COTO producto: {product}. \n Error: {e}")
        
        return products_with_prices
        
    @execution_time
    def get_all_prices(self):
        #Agregar a STORES en caso se agreguen nuevas funciones con otros supers
        data = {store: {} for store in STORES}
        for store in STORES:
            product_price = getattr(self, f"get_{store}_prices")()
            data[store] = product_price
        
        return data

    def normalize_data(self, data):
        actual_date = datetime.today().strftime("%d-%m-%Y %H:%M")
        data_rows = []
        
        for store, products in data.items():
            for product in products:
                data_rows.append({
                    'store': store,
                    'product': product[0], #Nombre producto
                    'price': product[1], #Precio
                    'date': actual_date
                })
        
        return data_rows
    
    def open_or_create(self, file_name, data):
        try:
            # Intentamos abrir el archivo en modo lectura
            df = pd.read_csv(f"{file_name}.csv")
            is_new = False
            print(f"Archivo {file_name} cargado correctamente.")
            
        except FileNotFoundError:
            # Si no se encuentra, lo creamos y retornamos un DataFrame vacío
            print(f"Archivo {file_name} no encontrado. Creando uno nuevo...")

            data_rows = self.normalize_data(data)
            
            df = pd.DataFrame(data_rows, columns=self.columns)
            is_new = True
            
        return df, is_new

    @execution_time
    def store_prices(self):
        data = self.get_all_prices()
        df, is_new =self.open_or_create(FILE_NAME, data)
        try:
            if is_new:
                df.to_csv(f'{FILE_NAME}.csv', index=False)
            else:
                data_rows = self.normalize_data(data)
                data_rows = pd.Series(data_rows)
                new_df = pd.DataFrame(data_rows.tolist())
                df = pd.concat([new_df, df], ignore_index=True)
                df.to_csv(f'{FILE_NAME}.csv', index=False)
        except Exception as e:
            print(f"Ocurrio un error: {e}")

