const solver = require('./solver');
const config = require('./config');

const multer = require('multer');
const bodyParser = require('body-parser');
const express = require('express');
const path = require('path');


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
  solver(req.file.path, sr => {
    res.sendFile(req.file.path + '.json');
  });
});


module.exports = app;
