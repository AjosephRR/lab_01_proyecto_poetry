
# notas.md

```md
# Notas del laboratorio

## Módulo
Arquitectura Limpia

## Objetivo técnico
Separar el módulo Orders en capas independientes, introducir Unit of Work para transacciones, usar un Presenter para desacoplar la salida del caso de uso y manejar el evento `OrderCreated` desde la capa de aplicación.

## Estructura del laboratorio
- `domain`: entidades, evento, puertos y UoW abstracto
- `application`: DTOs, presenter, dispatcher, handler y caso de uso
- `infrastructure`: repositorio en memoria y UoW concreto
- `interfaces`: controlador HTTP con FastAPI
- `tests`: pruebas por capa

## Componentes principales
- `Order` y `OrderItem`
- `OrderCreated`
- `CreateOrderUseCase`
- `JsonCreateOrderPresenter`
- `AbstractUnitOfWork`
- `InMemoryOrderRepository`
- `InMemoryUnitOfWork`
- `EventDispatcher`
- `OrderCreatedAuditHandler`

## Casos cubiertos con pruebas
- creación correcta de orden
- cálculo de total
- generación de evento de dominio
- persistencia mediante repositorio
- publicación del evento
- respuesta HTTP correcta

## Problemas corregidos durante el laboratorio
- estructura incompleta del paquete `application`
- faltaba el archivo `presenters.py`
- faltaba el subpaquete `application/use_cases`
- corrección de imports para que pytest pudiera recolectar y ejecutar pruebas
- separación de responsabilidades entre HTTP, aplicación y dominio

## Resultado final
Se dejó un flujo de creación de órdenes con arquitectura limpia, capas claras, evento de dominio, Unit of Work, Presenter y pruebas pasando correctamente.

## Aprendizaje técnico
Este laboratorio ayuda a entender cómo desacoplar reglas de negocio de frameworks, cómo introducir Unit of Work sin afectar el caso de uso, cómo usar Presenter para no amarrar la aplicación a HTTP y cómo manejar eventos de dominio en una arquitectura mantenible y migrable.