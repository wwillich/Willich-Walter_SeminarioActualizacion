
// ============================================
// 1. CONFIGURACIÓN DE LA API
// ============================================

// Dirección local del backend.
// Cuando publiquemos el proyecto, cambiaremos esta URL.
const API_URL = "https://portfolio-seminario-1.onrender.com";


// ============================================
// 2. ELEMENTOS DEL HTML
// ============================================

const formulario = document.getElementById("prediction-form");

const campoEdad = document.getElementById("age");
const campoBMI = document.getElementById("bmi");
const campoBP = document.getElementById("bp");

const boton = document.getElementById("submit-button");

const loading = document.getElementById("loading");
const resultado = document.getElementById("result");
const error = document.getElementById("error");

const campos = [campoEdad, campoBMI, campoBP];


// ============================================
// 3. VALIDACIONES DEL NAVEGADOR
// ============================================

// Personalizamos los mensajes de validación en español.

campos.forEach(campo => {

    campo.addEventListener("invalid", function() {

        if (campo.validity.valueMissing) {

            campo.setCustomValidity(
                "Este campo es obligatorio."
            );

        } else if (campo.validity.rangeUnderflow) {

            campo.setCustomValidity(
                "El valor ingresado está por debajo del mínimo permitido."
            );

        } else if (campo.validity.rangeOverflow) {

            campo.setCustomValidity(
                "El valor ingresado supera el máximo permitido."
            );

        } else if (campo.validity.badInput) {

            campo.setCustomValidity(
                "Ingresá un número válido."
            );

        } else {

            campo.setCustomValidity(
                "Revisá el valor ingresado."
            );

        }

    });

    // Eliminamos el mensaje anterior cuando el usuario modifica el campo.

    campo.addEventListener("input", function() {

        campo.setCustomValidity("");

    });

});


// ============================================
// 4. FUNCIONES AUXILIARES
// ============================================

// Oculta los mensajes anteriores.

function limpiarMensajes() {

    loading.classList.add("hidden");

    resultado.classList.add("hidden");

    error.classList.add("hidden");

}


// Muestra un mensaje de error.

function mostrarError(mensaje) {

    error.textContent = mensaje;

    error.classList.remove("hidden");

}


// Muestra el resultado de la predicción.

function mostrarResultado(datos) {

    resultado.textContent =
        `${datos.descripcion}: ${Number(datos.prediccion).toFixed(2)}`;

    resultado.classList.remove("hidden");

}


// ============================================
// 5. INTERPRETACIÓN DE ERRORES DE FASTAPI
// ============================================

function interpretarError(datos) {

    // Si el error no contiene una lista de validaciones.

    if (!Array.isArray(datos.detail)) {

        return datos.detail ||
            "No se pudieron validar los datos ingresados.";

    }

    // Traducimos los nombres de los campos.

    const nombres = {

        age: "Edad",

        bmi: "Índice de masa corporal",

        bp: "Presión arterial"

    };

    // Convertimos los errores técnicos en mensajes comprensibles.

    const mensajes = datos.detail.map(item => {

        const campo = item.loc?.[1];

        const nombre = nombres[campo] || "Dato ingresado";


        if (item.type === "missing") {

            return `${nombre}: este campo es obligatorio.`;

        }

        if (item.type === "less_than_equal") {

            return `${nombre}: supera el máximo permitido.`;

        }

        if (item.type === "greater_than") {

            return `${nombre}: está por debajo del mínimo permitido.`;

        }

        if (
            item.type === "int_type" ||
            item.type === "float_type"
        ) {

            return `${nombre}: debe ser un número válido.`;

        }

        return `${nombre}: revisá el valor ingresado.`;

    });

    return mensajes.join(" ");

}


// ============================================
// 6. VALIDACIÓN DE LOS DATOS
// ============================================

function validarDatos(datos) {

    // Validamos la edad.

    if (datos.age <= 0 || datos.age > 120) {

        mostrarError(
            "La edad debe ser mayor que 0 y no superar los 120 años."
        );

        campoEdad.focus();

        return false;

    }


    // Validamos el índice de masa corporal.

    if (datos.bmi <= 10 || datos.bmi > 70) {

        mostrarError(
            "El IMC debe ser mayor que 10 y no superar 70."
        );

        campoBMI.focus();

        return false;

    }


    // Validamos la presión arterial media.

    if (datos.bp <= 40 || datos.bp > 250) {

        mostrarError(
            "La presión arterial media debe ser mayor que 40 " +
            "y no superar 250 mmHg."
        );

        campoBP.focus();

        return false;

    }


    // Comprobamos que todos los valores sean números válidos.

    if (
        !Number.isFinite(datos.age) ||
        !Number.isFinite(datos.bmi) ||
        !Number.isFinite(datos.bp)
    ) {

        mostrarError(
            "Por favor, ingresá valores numéricos válidos."
        );

        return false;

    }

    return true;

}


// ============================================
// 7. ENVÍO DEL FORMULARIO
// ============================================

formulario.addEventListener("submit", async function(event) {

    // Evitamos que el navegador recargue la página.

    event.preventDefault();

    limpiarMensajes();


    // Convertimos los valores ingresados a números.

    const datos = {

        age: Number(campoEdad.value),

        bmi: Number(campoBMI.value),

        bp: Number(campoBP.value)

    };


    // Validamos los datos antes de enviarlos.

    if (!validarDatos(datos)) {

        return;

    }


    // Deshabilitamos el botón durante el procesamiento.

    boton.disabled = true;

    boton.textContent = "Procesando...";


    // Mostramos el mensaje de carga.

    loading.textContent =
        "Conectando con el servidor. La primera respuesta puede tardar unos segundos...";

    loading.classList.remove("hidden");


    // Configuramos un tiempo máximo de espera.

    const controlador = new AbortController();

    const temporizador = setTimeout(() => {

        controlador.abort();

    }, 75000);


    try {

        // Enviamos los datos al backend mediante fetch.

        const respuesta = await fetch(`${API_URL}/predecir`, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(datos),

            signal: controlador.signal

        });


        // Convertimos la respuesta del servidor a JSON.

        const contenido = await respuesta.json();


        // Comprobamos si el backend devolvió un error.

        if (!respuesta.ok) {

            if (respuesta.status === 422) {

                throw new Error(
                    interpretarError(contenido)
                );

            }


            if (respuesta.status === 500) {

                throw new Error(
                    "Ocurrió un error interno al realizar la estimación."
                );

            }


            throw new Error(
                contenido.detail ||
                "No se pudo obtener la estimación."
            );

        }


        // Si todo salió bien, mostramos la predicción.

        mostrarResultado(contenido);


    } catch (err) {

        // Registramos el error en la consola.

        console.error("Error de comunicación:", err);


        // Controlamos los distintos tipos de errores.

        if (err.name === "AbortError") {

            mostrarError(
                "El servidor tardó demasiado en responder. " +
                "Puede estar iniciándose. Intentá nuevamente."
            );

        } else if (err instanceof TypeError) {

            mostrarError(
                "No pudimos conectar con el servidor. " +
                "Verificá que la API esté funcionando."
            );

        } else {

            mostrarError(err.message);

        }


    } finally {

        // Cancelamos el temporizador.

        clearTimeout(temporizador);


        // Ocultamos el mensaje de carga.

        loading.classList.add("hidden");


        // Volvemos a habilitar el botón.

        boton.disabled = false;

        boton.textContent = "Obtener estimación";

    }

});
