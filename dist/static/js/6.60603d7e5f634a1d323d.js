webpackJsonp([6],{"4CE+":function(n,e,t){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=t("mtWM"),o=t.n(r),a={data:function(){return{randomNumber:0}},methods:{getRandomFromBackend:function(){var n=this;o.a.get("http://127.0.0.1:5000/api/random").then(function(e){n.randomNumber=e.data.randomNumber}).catch(function(n){console.log(n)})},getRandom:function(){this.randomNumber=this.getRandomFromBackend()}},created:function(){this.getRandom()}},m={render:function(){var n=this,e=n.$createElement,t=n._self._c||e;return t("div",[t("p",[n._v("Test RESTful API from Flask server")]),n._v(" "),t("p",[n._v("Random number from backend: "+n._s(n.randomNumber))]),n._v(" "),t("button",{on:{click:n.getRandom}},[n._v("New random number")])])},staticRenderFns:[]},d=t("VU/8")(a,m,!1,null,null,null);e.default=d.exports}});