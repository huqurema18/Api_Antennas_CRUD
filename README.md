### 1. /addCodSal [Método: POST]

Este endpoint permite agregar un nuevo código de sala a la colección CodeSalaAntenas.

#### Lógica:
- Recibe datos en formato JSON.
- Verifica si el `'codigo_clase'` ya existe en la colección.
  - Si no existe, inserta los datos y retorna un mensaje de éxito con el ID insertado.
  - Si existe, retorna un mensaje indicando que el código de sala ya existe.

#### Nota: 
- `'codigo_clase'` debe ser un número de hasta 6 dígitos.

#### Resultado: 
- Retorna un mensaje y, en caso de éxito, también retorna el ID del documento insertado.

### 2. /addStudent [Método: POST]

Este endpoint permite agregar un nuevo estudiante a la colección StudentsAntenas.

#### Lógica:
- Recibe datos en formato JSON.
- Verifica si el `'codigo_clase'` asociado existe en la colección CodeSalaAntenas.
  - Si existe, inserta los datos del estudiante y retorna un mensaje de éxito con el ID insertado.
  - Si no existe, retorna un mensaje indicando que el código de sala no existe.

#### Resultado: 
- Retorna un mensaje y, en caso de éxito, también retorna el ID del documento insertado.

### 3. /addComentario [Método: POST]

Este endpoint permite agregar un nuevo comentario a la colección ComentariosAntenas.

#### Lógica:
- Recibe datos en formato JSON.
- Inserta los datos y retorna un mensaje de éxito con el ID insertado.

#### Resultado: 
- Retorna un mensaje y el ID del documento insertado.

### 4. /getCodes [Método: GET]

Este endpoint permite recuperar todos los códigos de sala de la colección CodeSalaAntenas.

#### Resultado: 
- Retorna una lista de todos los códigos de sala.

### 5. /students [Método: GET]

Este endpoint permite recuperar todos los estudiantes de la colección StudentsAntenas.

#### Resultado: 
- Retorna una lista de todos los estudiantes.

### 6. /getStudents/<int:codigo_clase> [Método: GET]

Este endpoint permite recuperar estudiantes asociados a un `'codigo_clase'` específico.

#### Parámetro: 
- `'codigo_clase'` (hasta 6 dígitos).

#### Resultado: 
- Retorna una lista de estudiantes asociados al `'codigo_clase'` proporcionado.

### 7. /getComentary [Método: GET]

Este endpoint permite recuperar todos los comentarios de la colección ComentariosAntenas.

#### Resultado: 
- Retorna una lista de todos los comentarios.

### 8. /deleteStudents/<int:codigo_clase> [Método: DELETE]

Este endpoint permite eliminar estudiantes y el código de sala asociado a un `'codigo_clase'` específico.

#### Parámetro: 
- `'codigo_clase'` (hasta 6 dígitos).

#### Resultado: 
- Retorna un mensaje indicando la cantidad de estudiantes y códigos de sala eliminados.

### 9. /deleteCode/<int:codigo_clase> [Método: DELETE]

Este endpoint permite eliminar un código de sala y los estudiantes asociados a un `'codigo_clase'` específico.

#### Parámetro: 
- `'codigo_clase'` (hasta 6 dígitos).

#### Resultado: 
- Retorna un mensaje indicando la cantidad de códigos de sala y estudiantes eliminados.
