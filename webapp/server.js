// https://github.com/WeiChienHsu/webdevbootcamp/tree/master/AuthDemo/views

const express                 = require("express")    
const mongoose                = require("mongoose")
const passport                = require("passport")  
const bodyParser              = require("body-parser")   
const User                    = require("./models/user")    
const LocalStrategy           = require("passport-local")
const passportLocalMongoose   = require("passport-local-mongoose")
const app = express();

app.set('view engine','ejs');
mongoose.connect("mongodb://localhost:27017/accounts",
		 { useNewUrlParser: true ,  useUnifiedTopology: true});


app.use(bodyParser.urlencoded({extended:true}));
app.use(require("express-session")({
    secret:"secret",
    resave: false,
    saveUninitialized: false
}));


app.set('view engine','ejs');
//
app.use(passport.initialize());
app.use(passport.session());
// 
passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());



app.get('/', (req,res) => {
    res.render("home")
})

app.get('/home', isLoggedIn, (req,res) => {
    res.render("index",{name: req.user.username})
})



app.get("/register", function(req, res){
    res.render("register");
});


app.post("/register", function(req, res){
User.register(new User({username:req.body.username}),req.body.password, function(err, user){
       if(err){
            console.log(err);
            return res.render('register');
        } //user stragety
        passport.authenticate("local")(req, res, function(){
            res.redirect("/home"); //once the user sign up
       }); 
    });
});



app.get("/login", function(req, res){
    res.render("login");
})

// middleware
app.post("/login", passport.authenticate("local",{
    successRedirect:"/home",
    failureRedirect:"/login"
}),function(req, res){
    res.send("User is "+ req.user.id);
});

app.get("/logout", function(req, res){
    req.logout();
    res.redirect("/");
});


function isLoggedIn(req, res, next){
    if(req.isAuthenticated()){
        return next();
    }
    res.redirect("/login");
}


app.listen(5001)
