# Depth of Code

I came across this can.js method the other day at work:

    checkFeatures: function(features) {
        var self = this,
            isAllowed = false;
        return can.each(features, function() {
            return self.getFeature(this) ? (isAllowed = true, false) : undefined;
        }), isAllowed;
    }

#### Curiosity
First, `checkFeatures` is a method on a user model.

The `can.each` method is the Can.js implementation of the `each` method and takes the same arguments as a standard javascript object : `value`, `index`, `array`. It's purpose is to take a list of possible features and set `isAllowed` to true if any of at least one of the features is bound to `self`.  The context that you're lacking here is that these are sub-features, and they happen to determine whether their parent features, the top-level menu items, should be rendered at all.  An approach I'm not so sure about.

Anyway, even with that context, this method is a bit tricky to understand. I immediately re-wrote it before really comprehending it, but went through a few subsequent stages of emotion regarding its significance. Let's dive in.

```
var self = this;
```

Crockford is a notable advocate of this JavaScript idiom.  I assure you, though, in no possible world would he smile upon this code.  Saving `this` as `self` is a way of using values from multiple calling contexts in the same function.  Here, `self` preserves the context of the `checkFeatures` calling context so the `can.each` callback can refer to the `this` of the `checkFeatures` call in the process of iteration while also accepting the default `this` value provided to the context of `can.each`.  So far, so good.  That's what the whole `self` thing is for. 

But `return can.each(...), isAllowed` ? Really? Maybe in some Python-inspired language that cross-compiles to JavaScript this would return a tuple, but in vanilla JavaScript, the function only ever returns `isAllowed`.  

Also, using an `each` loop without the value when that is the obvious point of iteration through `features` is a little suspect.  

But finally, this line: 

`return self.getFeature(this) ? (isAllowed = true, false) : undefined;`

There's that comma operator again, but it's inside of a ternary's true branch this time.  If `self.getFeature(this)` returns true, then `isAllowed` is set to true, but the *ternary's* true branch, `(isAllowed = true, false)`, evaluates to `false`, which is how you break early from a `can.each` loop.  

Obscurantist, mischeivous, mystifying, etc.

Why the `undefined`? Did this person not want to *mislead* us by returning true? Would that be too obviously fucky? What's so wrong with returning `true` in the false branch (I mean, we've already returned `false` in the `true` branch ...) that this person had to return *undefined* instead?
