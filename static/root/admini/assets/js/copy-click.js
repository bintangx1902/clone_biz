const btn = document.getElementById('cop');
const url = '{{img.file.url}}';

btn.onclick = function () {
    url.select();
    document.execCommand("Copy");
}
