const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth2').Strategy;
const dotenv = require('dotenv');
const User = require('../api/models/User');
dotenv.config();
passport.use(new GoogleStrategy({
    clientID:     process.env.GOOGLE_CLIENT_ID,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    callbackURL: "http://localhost:3000/auth/google/callback",
    passReqToCallback   : true
  },
  async function(request, accessToken, refreshToken, profile, done)  {
    const user = await User.findOne({ email: profile.email });
    if (user) {
      return done(null, user);
    } else {
        const newUser = await User.create({
            googleId: profile.id,
            name: profile.displayName,
            email: profile.email,
            profile_pic: profile.picture,
            password: profile.id
        });
        return done(null, newUser);
    }
  }
));

passport.serializeUser(function(user, done) {
    done(null, user);
  }
);

passport.deserializeUser(function(user, done) {
    done(null, user);
  }
);

module.exports = passport;