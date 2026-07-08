from IPython.display import display
import pandas as pd

def exploratorio_df(
    df,
    n_muestra=5,
    mostrar_muestra=True,
    mostrar_tipos=True,
    mostrar_estadisticas=False,
    mostrar_nulos=True,
    mostrar_porcentaje_nulos=True,
    mostrar_unicos=True
):
    """
    Genera un informe exploratorio de un DataFrame.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame que se desea analizar.

    n_muestra : int, default=5
        Cantidad de registros aleatorios a mostrar.

    mostrar_muestra : bool, default=True
        Muestra una muestra aleatoria del DataFrame.

    mostrar_tipos : bool, default=True
        Muestra los tipos de datos de cada columna.

    mostrar_estadisticas : bool, default=False
        Muestra las estadísticas descriptivas del DataFrame.

    mostrar_nulos : bool, default=True
        Muestra la cantidad de valores nulos por columna.

    mostrar_porcentaje_nulos : bool, default=True
        Muestra el porcentaje de valores nulos por columna.

    mostrar_unicos : bool, default=True
        Muestra la cantidad de valores únicos por columna.
    """

    print("=" * 200)
    print("RESUMEN GENERAL")
    print("=" * 200)

    # Muestra aleatoria
    if mostrar_muestra:
        print("\nMUESTRA ALEATORIA")
        display(df.sample(n=min(n_muestra, len(df)), random_state=42))

    # Información general
    print("")
    print(f"\nFILAS      : {df.shape[0]:,}")
    print(f"COLUMNAS   : {df.shape[1]}")
    print(f"DUPLICADOS : {df.duplicated().sum():,}")
    print("")

    # Tipos de datos
    if mostrar_tipos:
        print("\nTIPOS DE DATOS")
        display(df.dtypes.to_frame().T)

    print("")
    # Estadísticas descriptivas
    if mostrar_estadisticas:
        print("\nESTADÍSTICAS BÁSICAS")
        display(df.describe(include="all"))

    # Valores nulos
    print("")
    if mostrar_nulos:
        df_nulos = df.isnull().sum().to_frame().T
        df_nulos.index = ["Valores nulos"]

        print("\nCANTIDAD DE VALORES NULOS POR COLUMNA")
        display(df_nulos)
    print("")

    # Porcentaje de nulos
    print("")
    if mostrar_porcentaje_nulos:
        df_nulos_pct = (df.isnull().mean() * 100).round(2).to_frame().T
        df_nulos_pct.index = ["% Valores nulos"]

        print("\nPORCENTAJE DE VALORES NULOS POR COLUMNA")
        display(df_nulos_pct)
    print("")

    # Valores únicos
    print("")
    if mostrar_unicos:
        df_unicos = df.nunique().to_frame().T
        df_unicos.index = ["Valores únicos"]

        print("\nCANTIDAD DE VALORES ÚNICOS POR COLUMNA")
        display(df_unicos)
