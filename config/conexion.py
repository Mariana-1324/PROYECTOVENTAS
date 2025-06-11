import mysql.connector

conexion = mysql.connector.connect(
    host="bqpwcgnzojllikvaaviz-mysql.services.clever-cloud.com",
    user="u8ygdtfrdso7mprj",
    password="02PXZqBPlbfaouN1YCfI",
    database="bqpwcgnzojllikvaaviz",
    use_pure=True
)
if conexion.is_connected():
    print("Conectado")