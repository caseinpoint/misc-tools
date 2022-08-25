// paste these in the console

const clickAll = () => {
    for (let button of document.querySelectorAll('button')) {
        if (button.classList.contains('courseExit') || 
            button.classList.contains('page-menu-toggle') ||
            button.classList.contains('nav-sidebar__outline-section-toggle')) {
                continue;
        }
        button.click();
    }
    setTimeout(() => { document.querySelector('.continue-btn').click(); }, 500);
};

const skip = () => {
    for (let vid of document.querySelectorAll('video')) {
        console.log(vid.id);
        vid.play();
        setTimeout(() => {
            vid.pause();
            vid.currentTime = vid.duration - 0.25;
            setTimeout(() => { vid.play(); }, 500)
        }, 500);
    }
};
