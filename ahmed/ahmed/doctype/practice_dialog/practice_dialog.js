// Copyright (c) 2024, ahmed and contributors
// For license information, please see license.txt

frappe.ui.form.on("Practice Dialog", {
  refresh: function (frm) {
    frm.add_custom_button("Open The Single Dialog", () => {
      let d = new frappe.ui.Dialog({
        title: "Enter details",
        fields: [
          {
            label: "First Name",
            fieldname: "first_name",
            fieldtype: "Data",
          },
          {
            label: "Last Name",
            fieldname: "last_name",
            fieldtype: "Data",
          },
          {
            label: "Age",
            fieldname: "age",
            fieldtype: "Int",
          },
        ],
        size: "small", // small, large, extra-large
        primary_action_label: "Submit",
        primary_action(values) {
          console.log(values);
          d.hide();
        },
      });

      d.show();
    });

    frm.add_custom_button("Open Single Notification", () => {
      // only message
      // frappe.msgprint(__("Document updated successfully"));

      // with options
      frappe.msgprint({
        title: __("Notification"),
        indicator: "green",
        message: __("Document updated successfully"),
      });
    });

    frm.add_custom_button("Primary Action", () => {
      // with primary action
      frappe.msgprint({
        title: __("Notification"),
        message: __("Are you sure you want to proceed?"),
        primary_action: {
          action(values) {
            console.log(values);
          },
        },
      });
    });

    frm.add_custom_button("Server Action Client Action", () => {
      // with server and client action
      frappe.msgprint({
        title: __("Notification"),
        message: __("Are you sure you want to proceed?"),
        primary_action: {
          label: "Proceed",
          // either one of the actions can be passed
          server_action: "dotted.path.to.method",
          client_action: "dotted_path.to_method",
          args: args,
        },
      });
    });

    frm.add_custom_button("Error Throw", () => {
      frappe.throw(__("This is an Error Message"));
    });
    frm.add_custom_button("Set title and button label", () => {
          // Set title and button label
          frappe.prompt("First Name", console.log, "Enter First Name", "Submit");

    });

    frm.add_custom_button("prompt for single value of type Data", () => {
      // prompt for single value of type Data
      frappe.prompt("First Name", ({ value }) => console.log(value));
    });
    frm.add_custom_button("prompt for single value of type Data", () => {``

  
      // prompt for single value of any type
      frappe.prompt(
        {
          label: "Birth Date",
          fieldname: "date",
          fieldtype: "Date",
        },
        
        (values) => {
          console.log(values.date);
        }
      );

     
    });

    frm.add_custom_button("prompt for multiple values", () => {
     // prompt for multiple values
     frappe.prompt(
      [
        {
          label: "First Name",
          fieldname: "first_name",
          fieldtype: "Data",
        },
        {
          label: "Last Name",
          fieldname: "last_name",
          fieldtype: "Data",
        },
      ],
      (values) => {
        console.log(values.first_name, values.last_name);
      }
    );
    });
    frm.add_custom_button("YES/NO then do this", () => {
      frappe.confirm('Are you sure you want to proceed?',
        () => {
            // action to perform if Yes is selected
            frappe.msgprint("action to perform if Yes is selected")
        }, () => {
            // action to perform if No is selected
            frappe.msgprint("action to perform if No is selected")

        })
     });
     frm.add_custom_button("YES/NO then do this", () => {
      frappe.confirm('Are you sure you want to proceed?',
        () => {
            // action to perform if Yes is selected
            frappe.msgprint("action to perform if Yes is selected")
        }, () => {
            // action to perform if No is selected
            frappe.msgprint("action to perform if No is selected")

        })
     });
     frm.add_custom_button("YES/NO then do this", () => {
      frappe.confirm('Are you sure you want to proceed?',
        () => {
            // action to perform if Yes is selected
            frappe.msgprint("action to perform if Yes is selected")
        }, () => {
            // action to perform if No is selected
            frappe.msgprint("action to perform if No is selected")

        })
     });
     frm.add_custom_button("Warning Message", () => {
      frappe.confirm('Are you sure you want to proceed?',
          () => {
              frappe.warn('Are you sure you want to proceed?',
                  'There are unsaved changes on this page',
                  () => {
                      // action to perform if Continue is selected
                      frappe.msgprint("Action to perform if Yes is selected");
                  },
                  'Continue',
                  true // Sets dialog as minimizable
              );
          }
      );
  
    });
  
  },
});
