const exec = require('child_process').exec;
const path = require('path');

const SCRIPT_PATH = path.join(__dirname, '..', 'scripts', 'find_similar.py');
const EXEC_PREFIX = 'python ' + SCRIPT_PATH;


function solver(imgPath, callback) {
  var command = EXEC_PREFIX + ' ' + imgPath;
  exec(command, function (error, stdout, stderr) {
    if (error !== null) {
      console.log('ERROR, bro!');
      console.log(error);
      callback({ error: error });
    }
    console.log('Solved ' + imgPath);
    callback('ok');
  });
}

module.exports = solver;
