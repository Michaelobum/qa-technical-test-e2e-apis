Pasos para ejecutar las pruebas de APIs (Karate + PetStore)

1. Requisitos:
   - Java 17 (o 11+)
   - Maven 3.x

2. Clonar el repositorio y entrar en la carpeta:
   cd apis_petstore_karate

3. Ejecutar pruebas:
   mvn test
   (o mvn -Dtest=PetstoreUsersRunner test)

4. Reportes:
   - target/karate-reports
   - target/surefire-reports

Los escenarios implementados:
   - Crear un usuario en PetStore
   - Buscar el usuario creado
   - Actualizar nombre y correo del usuario
   - Buscar el usuario actualizado
   - Eliminar el usuario y verificar que ya no exista
