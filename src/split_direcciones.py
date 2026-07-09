from IPython.display import display
import pandas as pd

def separar_direccion(direccion):
    """
    Separa una dirección completa en tres componentes:
    calle, ciudad y estado_zip.

    La función maneja direcciones con un número variable de comas.
    Si la calle contiene comas adicionales (por ejemplo, "Suite 200"),
    estas se conservan como parte de la calle.

    Cuando el código postal no está presente, se reemplaza por
    'NO_ZIP' para indicar explícitamente que el dato no fue registrado.

    Parámetros
    ----------
    direccion : str
        Dirección completa del restaurante.

    Retorna
    -------
    pandas.Series
        Serie con tres elementos:
        - calle
        - ciudad
        - estado_zip
    """

    # Si la dirección es nula, retorna tres valores nulos
    if pd.isna(direccion):
        return pd.Series([None, None, None])

    # Divide la dirección por comas y elimina espacios en blanco
    partes = [p.strip() for p in direccion.split(",")]

    # Caso donde existen al menos calle, ciudad, estado y código postal
    if len(partes) >= 4:

        # La calle puede contener una o más comas, por lo que se reconstruye
        calle = ", ".join(partes[:-3])

        # La ciudad corresponde al tercer elemento desde el final
        ciudad = partes[-3]

        # Extrae el estado y el código postal
        estado = partes[-2]
        zip_code = partes[-1]

        # Si el código postal está vacío, asigna un valor descriptivo
        if zip_code:
            estado_zip = f"{estado}, {zip_code}"
        else:
            estado_zip = f"{estado}, NO_ZIP"

    # Caso donde solo existen calle, ciudad y estado
    elif len(partes) == 3:

        calle = partes[0]
        ciudad = partes[1]
        estado_zip = partes[2]

    # Caso de direcciones con un formato inesperado
    else:

        # Conserva la dirección original y deja vacías las demás columnas
        calle = direccion
        ciudad = None
        estado_zip = None

    # Devuelve las tres columnas como una Serie de Pandas
    return pd.Series([calle, ciudad, estado_zip])