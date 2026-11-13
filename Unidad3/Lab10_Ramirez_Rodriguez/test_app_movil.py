import pytest
from app_movil import PerfilMovil, PerfilPro, SuscripcionExpiradaError, PuntosInsuficientesError

@pytest.fixture
def perfil_standard():
    return PerfilMovil(username="Leo", gemas=50)

@pytest.fixture
def perfil_pro_activo():
    return PerfilPro(username="Leonardo", gemas=100, meses_suscripcion=3)

def test_perfil_movil_atributos_iniciales(perfil_standard):
    assert perfil_standard.username == "Leo"
    assert perfil_standard.gemas == 50
    assert perfil_standard.racha_dias == 1
    assert perfil_standard.notificaciones_activas is True

def test_perfil_movil_inicializacion_gemas_negativas():
    with pytest.raises(ValueError):
        PerfilMovil(username="test_user", gemas=-10)

def test_perfil_pro_atributos_iniciales(perfil_pro_activo):
    assert perfil_pro_activo.username == "Leonardo"
    assert perfil_pro_activo.gemas == 100
    assert perfil_pro_activo.meses_suscripcion == 3
    assert perfil_pro_activo.es_pro is True

def test_perfil_pro_meses_suscripcion_invalido():
    with pytest.raises(ValueError):
        PerfilPro(username="pro_invalido", gemas=50, meses_suscripcion=0)

    with pytest.raises(ValueError):
        PerfilPro(username="pro_invalido", gemas=50, meses_suscripcion=-2)

#Pruebas de métodos 
def test_ganar_gemas_exito(perfil_standard):
    nuevo_balance = perfil_standard.ganar_gemas(25)
    assert nuevo_balance == 75
    assert perfil_standard.gemas == 75

def test_gastar_gemas_exito(perfil_standard):
    nuevo_balance = perfil_standard.gastar_gemas(20)
    assert nuevo_balance == 30
    assert perfil_standard.gemas == 30

def test_descargar_contenido_offline_exito(perfil_pro_activo):
    resultado = perfil_pro_activo.descargar_contenido_offline()
    assert resultado == "Contenido descargado para uso offline."

#Control y propagación de excepciones 
def test_ganar_gemas_cantidad_invalida(perfil_standard):
    with pytest.raises(ValueError):
        perfil_standard.ganar_gemas(0)

    with pytest.raises(ValueError):
        perfil_standard.ganar_gemas(-15)

def test_gastar_gemas_cantidad_invalida(perfil_standard):
    with pytest.raises(ValueError):
        perfil_standard.gastar_gemas(0)

    with pytest.raises(ValueError):
        perfil_standard.gastar_gemas(-10)

def test_gastar_gemas_puntos_insuficientes(perfil_standard):
    with pytest.raises(PuntosInsuficientesError):
        perfil_standard.gastar_gemas(100)

def test_descargar_contenido_offline_suscripcion_expirada():
    perfil_pro = PerfilPro(username="user_expirado", gemas=50, meses_suscripcion=1)
    perfil_pro.meses_suscripcion = 0 

    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()

    assert perfil_pro.es_pro is False

#Pruebas parametrizadas 
@pytest.mark.parametrize("monto_ganado, balance_esperado", [
    (1, 51),
    (10, 60),
    (100, 150),
    (500, 550)
])
def test_ganar_gemas_parametrizado(perfil_standard, monto_ganado, balance_esperado):
    assert perfil_standard.ganar_gemas(monto_ganado) == balance_esperado

@pytest.mark.parametrize("monto_invalido", [0, -1, -50, -100])
def test_ganar_gemas_invalidos_parametrizado(perfil_standard, monto_invalido):
    with pytest.raises(ValueError):
        perfil_standard.ganar_gemas(monto_invalido)

#Verificación de jerarquía de clases y tipos 
def test_jerarquia_y_herencia_perfil_pro(perfil_pro_activo):
    assert isinstance(perfil_pro_activo, PerfilPro)
    assert isinstance(perfil_pro_activo, PerfilMovil)
    assert isinstance(SuscripcionExpiradaError(), Exception)
    assert isinstance(PuntosInsuficientesError(), Exception)