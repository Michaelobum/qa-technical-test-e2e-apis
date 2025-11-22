=============================================================================
PROYECTO: AUTOMATIZACIÓN DE APIS - PETSTORE (OPCIÓN 3)
=============================================================================

DESCRIPCIÓN:
Este proyecto automatiza el ciclo de vida completo (CRUD) de usuarios en la API
de PetStore (https://petstore.swagger.io/).
Implementado con Karate DSL y Java.

El escenario "Flujo completo de usuario" incluye:
1. Creación de usuario con datos dinámicos (UUID).
2. Consulta del usuario creado.
3. Actualización de nombre y correo.
4. Verificación de la actualización.
5. Eliminación del usuario y validación de inexistencia (404).

REQUISITOS PREVIOS:
- Java JDK 11 o superior.
- Apache Maven instalado y configurado en el PATH.

INSTRUCCIONES DE EJECUCIÓN:
1. Abrir una terminal en la carpeta raíz del proyecto 'apis'.
2. Ejecutar el siguiente comando Maven:

   mvn test "-Dtest=petstore.users.UsersRunner"

VERIFICACIÓN DE RESULTADOS (REPORTES):
Al finalizar la ejecución, se genera un reporte HTML detallado automáticamente.
Puede visualizarlo abriendo el siguiente archivo en su navegador:

   apis/target/karate-reports/karate-summary.html

EVIDENCIA:
El reporte incluye los Payloads (Request) y las Respuestas (Response) de cada
interacción con la API, validando los códigos de estado HTTP y la integridad
de los datos mediante 'match assertions'.

AUTOR:
Michael Eduardo Morán Naranjo