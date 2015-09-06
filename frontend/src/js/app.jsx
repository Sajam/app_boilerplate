var $ = require('jquery');
var React = require('react');
var Foo = require('./components/foo.jsx');

$(function () {
	React.render(<Foo />, $('#wrapper')[0]);
});
