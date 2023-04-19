function togglemodal(target) {
    let targetdisplay = document.getElementById(target);
    switch(targetdisplay.style.display) {
        case 'block':
            targetdisplay.style.display = 'none';
            break;
        case 'none':
            targetdisplay.style.display = 'block';
            break;
    }
}

function getChoice(e, modaltarget, inputtarget) {
    let target_input = document.getElementById(inputtarget);
    switch(e.type) {
        case 'button':
            target_input.value = e.innerHTML;
            break;

    }
    togglemodal(modaltarget);
}
