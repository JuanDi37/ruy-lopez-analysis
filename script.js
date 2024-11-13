async function main() {
    // Cargar Pyodide
    let pyodide = await loadPyodide();
    // Cargar las bibliotecas necesarias
    await pyodide.loadPackage(['numpy', 'pandas', 'matplotlib', 'networkx', 'seaborn']);

    // Obtener referencias a los botones
    const btnGrafo = document.getElementById('btn-grafo');
    const btnHeatmap = document.getElementById('btn-heatmap');
    const outputDiv = document.getElementById('output');

    // Código Python adaptado como cadena
    const codigoPython = `
# (Aquí se coloca el código Python adaptado, asegurándose de que sea compatible con Pyodide)
    `;

    // Función para ejecutar código Python
    async function ejecutarCodigoPython(codigo) {
        await pyodide.runPythonAsync(codigo);
    }

    // Evento para generar el grafo
    btnGrafo.addEventListener('click', async () => {
        outputDiv.innerHTML = '<p>Generando grafo...</p>';
        await ejecutarCodigoPython(`
${codigoPython}

// Llamar a la función para visualizar el grafo
visualizar_grafo(matriz_probabilidades)
        `);
        outputDiv.innerHTML = '<p>Grafo generado.</p>';
    });

    // Evento para generar el heatmap
    btnHeatmap.addEventListener('click', async () => {
        outputDiv.innerHTML = '<p>Generando heatmap...</p>';
        await ejecutarCodigoPython(`
${codigoPython}

// Llamar a la función para visualizar el heatmap
visualizar_heatmap(matriz_probabilidades)
        `);
        outputDiv.innerHTML = '<p>Heatmap generado.</p>';
    });
}

main();