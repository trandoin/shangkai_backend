require('dotenv').config();
const path = require('path');
const User = require('./api/models/User');
const express = require('express');
var session = require('express-session');
const mongoose = require('mongoose');
const MongoDBStore = require('connect-mongodb-session')(session);
const store = new MongoDBStore({
    uri: 'mongodb://localhost:27017/google_auth',
    collection: 'mySessions'
});

// Catch errors
store.on('error', function(error) {
    console.log(error);
  });


const passport = require('./config/passport');
const login_middleware = require('./api/middlewares/login');
const app = express();
app.use(express.static(path.join(__dirname, 'public')));
app.use(session({
  secret: process.env.SESSION_SECRET,
  cookie: {
    maxAge: 1000 * 60 * 60 * 24 * 7 // 1 week
  },
  resave: true,
  saveUninitialized: true,
  store: store
}));
app.use(passport.initialize());
app.use(passport.session());
app.use(express.urlencoded({extended:false}));


app.get('/', (req, res) => {
    res.send(`
    <h1>Google Auth</h1>
    <br><br>
    <h3>Login using credentials
    <form action="/login" method="POST">
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="submit" value="Log In">
    </form>
    <h3>Or</h3>
    <a href="/auth/google">Login with Google</a>
    <br><br>
    <h3>Or</h3>
    <a href="register">create an account</a>
    <form action="/register" method="POST">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="submit" value="Signup">
    </form>
    `);
    }
);

app.get('/auth/google', 
passport.authenticate(
    'google', { 
        scope: [ 'email', 'profile' ]
    }
));
app.get( '/auth/google/callback',
  passport.authenticate( 'google', {
    successRedirect: '/protected',
    failureRedirect: '/auth/google/failure'
  })
);
app.get('/logout', function(req, res, next) {
    req.logout(function(err) {
      if (err) { return next(err); }
      req.session.destroy();
      res.redirect('/');
    });
  });
app.get('/auth/google/failure', (req, res) => {
    res.send('Failed to authenticate..');
  });

app.get('/protected',login_middleware.isLoggedIn, (req, res) => {
    res.send(`<h1>Hello ${req.user.name}!</h1>
    <img src="${req.user.profile_pic}" alt="profile pic" />
    <br><br>
    <a href="/logout">Logout</a>`);
    }
);

app.post('/login', (req,res) => {
    const email = req.body.email;
    const password = req.body.password;
    User.findOne({email:email}, (err, user) => {
        if (err) {
            console.log(err);
            res.redirect('/');
        } else {
            if (!user) {
                res.send('no such user found');
            } else {
                if(user.password === password) {
                    req.login(user, function(err) {
                        if (err) { return next(err); }
                        return res.redirect('/protected');
                        });
                } else {
                    res.send('wrong password');
                }
            }
        }
    });
});

app.post('/register', (req,res) => {
    const name = req.body.name;
    const email = req.body.email;
    const password = req.body.password;
    User.findOne({email:email}, (err, user) => {
        if (err) {
            console.log(err);
            res.redirect('/');
        } else {
            if (!user) {
                const newUser = new User({
                    name: name,
                    email: email,
                    password: password
                });
                newUser.save((err) => {
                    if (err) {
                        console.log(err);
                        res.redirect('/');
                    } else {
                        res.send('user created');
                    }
                });
            } else {
                res.send('user already exists');
            }
        }
    });
});



mongoose.connect('mongodb://localhost:27017/google_auth', { useNewUrlParser: true, useUnifiedTopology: true })
.then(() => {
    console.log('Connected to MongoDB');
})
.catch((err) => {
    console.log('Error connecting to MongoDB', err);
});

app.listen(3000, () => {
    console.log('Listening on port 3000');
    }
);