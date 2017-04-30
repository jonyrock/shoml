const express = require('express')
const bodyParser = require('body-parser');
const path = require('path');
const multer = require('multer');
const config = require('./config')


const PATH_CLIENT = path.join(__dirname, 'client', 'dist');

var app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/static', express.static(path.join(PATH_CLIENT, 'static')));

app.get('/', function (req, res) {
  res.sendFile(path.join(PATH_CLIENT, 'index.html'));
});


const upload = multer({ dest: config.uploadsPath });
app.post('/upload/', upload.single('file'), function(req, res) {
  console.log('uploaded a file');
  console.log(req.file.path);
});


module.exports = app;
