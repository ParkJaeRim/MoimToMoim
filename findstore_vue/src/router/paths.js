export default [
    {
      path: "",
      view: "Home",
      name: "home"
    },
    // 유저
    {
      path: "/login",
      view: "accounts/Login",
      name: "login"
    },
    {
      path: "/signup",
      view: "accounts/Signup",
      name: "signup"
    },
    // Article
    {
      path: "/article",
      view: "articles/ArticleList",
      name: "articlelist"
    },
    // meeting
    {
      path: "/meeting",
      view: "meeting/MeetingList",
      name: "meetinglist"
    },
    // stores
    {
      path: "/store",
      view: "stores/StoreDetail",
      name: "storedetail"
    },
  ];
  