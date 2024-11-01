import classNames from "classnames";
import React from "react";
import styles from "./StyledTable.module.css";

// export const StyledTableWrapper = ({ children }) => {  
//   return <div className={styles.tableWrapper}>{children}</div>;
// };

export const StyledTableWrapper = ({ children , header = "primary"}) => {  
  return <div className={classNames(styles.tableWrapper, {
    [styles.tableHeaderPrimary]: header === "primary",
    [styles.tableHeaderSecondary]: header === "secondary",
  })}>{children}</div>;
};

