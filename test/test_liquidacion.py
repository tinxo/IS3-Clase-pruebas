# Archivo con los tests unitarios

# python -m pip install pytest
# conda install pytest

import pytest
import app.liquidacion as lq

def setup():
    # Se define en esta clase una instancia de la clase a testear
    instancia = lq.Liquidacion()
    return instancia

def test_instancia_basica():
    un_empleado = setup()
    assert un_empleado.valor_hora == 550
    assert un_empleado.pct_bonificacion == 8
    assert un_empleado.pct_retenciones == 11
    assert un_empleado.pct_obraSocial == 3

def test_calcular_sueldo_basico():
    un_empleado = setup()
    hs_trabajadas = 40
    assert un_empleado.calcular_sueldo_basico(hs_trabajadas) == 22000.00

def test_calcular_sueldo_bruto():
    un_empleado = setup()
    basico = 22000
    antiguedad = 3
    assert un_empleado.calcular_sueldo_bruto(basico, antiguedad) == 25960.00

def test_calcular_sueldo_neto():
    un_empleado = setup()
    bruto = 25960
    assert un_empleado.calcular_sueldo_neto(bruto) ==  22325.60

def test_calcular_sueldo_empleado():
    un_empleado = setup()
    hs_trabajadas = 40
    antiguedad = 3
    assert un_empleado.calcular_sueldo_empleado(hs_trabajadas, antiguedad) == 22325.60

def test_integrado():
    un_empleado = setup()
    hs_trabajadas = 400
    hs_trabajadas2 = 40
    antiguedad = 3
    total_fc = un_empleado.calcular_sueldo_empleado(hs_trabajadas, antiguedad)
    
    basico = un_empleado.calcular_sueldo_basico(hs_trabajadas2)    
    bruto = un_empleado.calcular_sueldo_bruto(basico, antiguedad)
    total_fs = un_empleado.calcular_sueldo_neto(bruto)

    assert total_fc == total_fs