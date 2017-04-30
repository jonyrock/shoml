const express = require('express')
const bodyParser = require('body-parser');
const path = require('path');
const multer = require('multer');
const config = require('./config')


const PATH_CLIENT = path.join(__dirname, 'client', 'dist');
const PATH_UPLOAD = path.join(__dirname, 'uploads');


var app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/static', express.static(path.join(PATH_CLIENT, 'static')));

app.get('/', function (req, res) {
  res.sendFile(path.join(PATH_CLIENT, 'index.html'));
});

const upload = multer({ dest: PATH_UPLOAD });
app.post('/upload/', upload.single('file'), function(req, res) {
  console.log('uploaded a file');
  console.log(req.file.path);
  res.send('ok');
});


module.exports = app;
