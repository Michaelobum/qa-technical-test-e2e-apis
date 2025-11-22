Feature: Gestión de usuarios en PetStore

  Background:
    * def baseUrl = 'https://petstore.swagger.io/v2'
    * url baseUrl

  Scenario: Flujo completo de usuario (Crear, Leer, Actualizar, Eliminar)
    # --- PREPARACIÓN DE DATOS ---
    * def randomUuid = java.util.UUID.randomUUID().toString()
    * def userName = 'qa_user_' + randomUuid
    # Definimos el payload inicial en una variable para reutilizar o modificar
    * def userPayload =
      """
      {
        "id": 0,
        "username": "#(userName)",
        "firstName": "QA",
        "lastName": "User",
        "email": "qa_user@test.com",
        "password": "123456",
        "phone": "123456789",
        "userStatus": 1
      }
      """

    # --- 1. CREAR UN USUARIO ---
    Given path 'user'
    And request userPayload
    When method post
    Then status 200
    * print '>>> RESPUESTA CREACION:', response

    # --- 2. BUSCAR EL USUARIO CREADO ---
    Given path 'user', userName
    When method get
    Then status 200
    And match response.username == userName
    And match response.email == 'qa_user@test.com'

    # --- 3. ACTUALIZAR NOMBRE Y CORREO ---
    # Modificamos el payload original
    * set userPayload.firstName = 'QA_Updated'
    * set userPayload.email = 'qa_updated@test.com'
    
    Given path 'user', userName
    And request userPayload
    When method put
    Then status 200
    * print '>>> PAYLOAD ENVIADO:', userPayload
    
    # --- 4. BUSCAR EL USUARIO ACTUALIZADO ---
    Given path 'user', userName
    When method get
    Then status 200
    # Validamos que los cambios se aplicaron
    And match response.firstName == 'QA_Updated'
    And match response.email == 'qa_updated@test.com'

    # --- 5. ELIMINAR EL USUARIO ---
    Given path 'user', userName
    When method delete
    Then status 200

    # --- VALIDAR QUE YA NO EXISTE ---
    Given path 'user', userName
    When method get
    Then status 404