var gulp = require('gulp');
var source = require('vinyl-source-stream');
var browserify = require('browserify');
var reactify = require('reactify');
var sass = require('gulp-sass');


var environmentConfig = {
	development: {
		debug: true,
		dest: './frontend/build'
	},
	production: {
		debug: false,
		dest: './frontend/dist'
	}
};


var browserifyTask = function (config) {
	browserify({
			entries: ['./frontend/src/js/app.jsx'],
			debug: config.debug
		})
		.transform(reactify)
	    .bundle()
        .pipe(source('app.js'))
        .pipe(gulp.dest(config.dest));
};

var sassTask = function (config) {
	gulp.src('./frontend/src/scss/**/*.scss')
		.pipe(sass())
		.pipe(gulp.dest(config.dest));
};


gulp.task('default', function () {
	browserifyTask(environmentConfig.development);
	sassTask(environmentConfig.development);
});

gulp.task('deploy', function () {
	browserifyTask(environmentConfig.production);
	sassTask(environmentConfig.development);
});
