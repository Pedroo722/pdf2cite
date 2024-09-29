function addInput() {
    const fileInputsContainer = document.getElementById('fileInputs');
    const newFileInput = document.createElement('div');
    newFileInput.classList.add('file-label', 'mb-3');
    newFileInput.innerHTML = `
        <label class="custom-file-upload">
            <input type="file" name="files" class="file-input" required onchange="updateFileName(this)">
            Inserir Arquivo
        </label>
        <span class="file-name">Nenhum arquivo selecionado</span>
        <button type="button" class="btn btn-danger remove-btn" onclick="removeInput(this)">X</button>
    `;
    fileInputsContainer.appendChild(newFileInput);
}

function removeInput(button) {
    const inputField = button.parentElement;
    inputField.remove(); 
}

function updateFileName(input) {
    const fileNameLabel = input.parentElement.nextElementSibling; 
    const fileName = input.files.length > 0 ? input.files[0].name : "Nenhum arquivo selecionado";
    fileNameLabel.innerText = fileName; 
}

function copyCitation(button) {
    const citationText = button.previousElementSibling.innerText;
    navigator.clipboard.writeText(citationText)
        .then(() => {
            alert('Citação copiada para a área de transferência!');
        })
        .catch(err => {
            console.error('Erro ao copiar: ', err);
        });
}
