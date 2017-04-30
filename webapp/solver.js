const exec = require('child_process').exec;
const path = require('path');

const SCRIPT_PATH = path.join(__dirname, '..', 'scripts', 'find_image_id.py');
const EXEC_PREFIX = 'python ' + SCRIPT_PATH;


function solver(imgPath, callback) {
  var command = EXEC_PREFIX + ' ' + imgPath;
  exec(command, function (error, stdout, stderr) {
    if (error !== null) {
      callback({ error: error });
    }
    var id = +stdout;
    console.log('Solved ' + imgPath + ' -> ' + id);
    callback({ id: +stdout });
  });
}

module.exports = solver;
