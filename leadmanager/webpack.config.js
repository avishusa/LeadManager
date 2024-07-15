const path = require('path');

module.exports = {
  mode: 'development',
  entry: './leadmanager/frontend/src/index.js',
  output: {
    path: path.resolve(__dirname, 'frontend/static/frontend'),
    filename: 'main.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  watch: true,
};
