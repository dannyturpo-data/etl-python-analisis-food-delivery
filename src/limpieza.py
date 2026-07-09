from IPython.display import display
import pandas as pd

def limpieza(df):
    """
    Realiza la limpieza y transformación del DataFrame de menús.

    Transformaciones realizadas:
    1. Convierte la columna 'price' de texto a float.
    2. Elimina registros con precio nulo o igual a 0.
    3. Reemplaza las descripciones nulas por 'sin descripcion'.
    4. Estandariza a minúsculas las columnas category, name y description.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame con la información del menú.

    Retorna
    -------
    pandas.DataFrame
        DataFrame limpio y transformado.
    """

    # Trabajar sobre una copia para no modificar el DataFrame original
    df = df.copy()

    # ------------------------------------------------------------------
    # 1. Limpiar y convertir la columna price
    # Ej: "15,99 USD" -> 15.99
    # ------------------------------------------------------------------
    df["price"] = (
        df["price"]
        .str.replace(" USD", "", regex=False)
        .str.replace(",", ".", regex=False)
    )

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # ------------------------------------------------------------------
    # 2. Eliminar registros con precio nulo o igual a 0
    # ------------------------------------------------------------------
    df = df.dropna(subset=["price"])
    df = df[df["price"] != 0]

    # ------------------------------------------------------------------
    # 3. Completar descripciones nulas
    # ------------------------------------------------------------------
    df["description"] = (
        df["description"]
        .fillna("sin descripcion")
    )

    # ------------------------------------------------------------------
    # 4. Estandarizar texto
    # ------------------------------------------------------------------
    columnas_texto = ["category", "name", "description"]

    df[columnas_texto] = (
        df[columnas_texto]
        .apply(lambda columna: columna.str.strip().str.lower())
    )

    return df